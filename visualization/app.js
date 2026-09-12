const links = linkRelations.map(
  ([source, target, type, direction = 'forward']) => ({
    source,
    target,
    type,
    direction,
  }),
);
const svg = d3.select('#map');
const mapFrame = document.querySelector('.map-frame');
const tooltip = d3
  .select(mapFrame)
  .append('div')
  .attr('class', 'node-tooltip')
  .attr('role', 'tooltip')
  .attr('aria-hidden', 'true');
let width = 800;
let height = 610;
let activeDomains = new Set(['all']);
let selectedId = null;
let simulation;

function render() {
  width = mapFrame.clientWidth;
  height = window.innerWidth < 900 ? 570 : 610;
  initializeViewBox(width, height);
  const g = svg.append('g');
  const defs = svg.append('defs');
  defs
    .append('marker')
    .attr('id', 'arrow')
    .attr('viewBox', '0 -5 10 10')
    .attr('refX', 8)
    .attr('refY', 0)
    .attr('markerWidth', 7)
    .attr('markerHeight', 7)
    .attr('orient', 'auto-start-reverse')
    .append('path')
    .attr('d', 'M0,-4L10,0L0,4Z')
    .attr('fill', 'context-stroke');

  const zoom = d3
    .zoom()
    .scaleExtent([0.65, 2.6])
    .on('zoom', (event) => g.attr('transform', event.transform));

  svg.call(zoom);

  const visibleNodes = nodes.filter(
    (node) =>
      activeDomains.has('all') ||
      activeDomains.has(node.domain) ||
      activeDomains.has(node.role),
  );

  const visibleIds = new Set(visibleNodes.map((node) => node.id));

  const endpointId = (endpoint) =>
    typeof endpoint === 'string' ? endpoint : endpoint.id;

  const visibleLinks = links
    .filter(
      (link) =>
        visibleIds.has(endpointId(link.source)) &&
        visibleIds.has(endpointId(link.target)),
    )
    .map((link) => ({
      ...link,
      source: endpointId(link.source),
      target: endpointId(link.target),
    }));

  document.querySelector('#visible-count').textContent =
    `${visibleNodes.filter((node) => node.role === 'node').length} nodes + ${visibleNodes.filter((node) => node.role === 'inter-stem').length} inter-stem / ${visibleLinks.length} relations`;

  const linkHitArea = g
    .append('g')
    .attr('class', 'link-hit-areas')
    .selectAll('line')
    .data(visibleLinks)
    .join('line')
    .attr('class', 'link-hit')
    .attr('tabindex', 0)
    .attr('aria-label', (d) => relationLabel(d))
    .on('mouseenter', (event, d) => showRelationTooltip(event, d))
    .on('mousemove', (event) => moveTooltip(event))
    .on('mouseleave', hideTooltip)
    .on('focus', (event, d) => showRelationTooltip(event, d))
    .on('blur', hideTooltip);

  const link = g
    .append('g')
    .attr('class', 'links')
    .selectAll('line')
    .data(visibleLinks)
    .join('line')
    .attr('class', (d) => {
      return `link ${relationCategories[d.type]}`;
    })
    .attr('marker-end', 'url(#arrow)')
    .attr('marker-start', 'url(#arrow)');

  const node = g
    .append('g')
    .attr('class', 'nodes')
    .selectAll('g')
    .data(visibleNodes, (d) => d.id)
    .join('g')
    .attr(
      'class',
      (d) =>
        `node node-${d.colorDomain || d.domain} ${d.role === 'inter-stem' ? 'inter-stem' : 'ordinary-node'}`,
    )
    .attr('aria-label', (d) => d.label)
    .attr('tabindex', 0)
    .on('mouseenter', (event, d) => {
      d3.select(event.currentTarget).raise();
      showTooltip(event, d);
    })
    .on('mousemove', (event) => moveTooltip(event))
    .on('mouseleave', hideTooltip)
    .on('focus', (event, d) => {
      d3.select(event.currentTarget).raise();
      showTooltip(event, d);
    })
    .on('blur', hideTooltip)
    .on('click', (_, d) => selectNode(d))
    .call(
      d3
        .drag()
        .on('start', dragStarted)
        .on('drag', dragged)
        .on('end', dragEnded),
    );

  node.each(function (d) {
    const shape = d3.select(this);
    shape.append('circle').attr('r', d.size);
  });

  node
    .append('text')
    .attr('x', (d) => d.size + 7)
    .attr('y', -3)
    .each(function (d) {
      const label = d3.select(this);
      const parts = d.shortLabel.split(': ');
      parts.forEach((part, index) =>
        label
          .append('tspan')
          .attr('x', d.size + 7)
          .attr('dy', index === 0 ? 0 : 14)
          .text(index === 0 && parts.length > 1 ? `${part}:` : part),
      );
    });

  node
    .append('text')
    .attr('class', 'node-kind')
    .attr('x', (d) => d.size + 7)
    .attr('y', 11)
    .text((d) => d.kind);

  simulation = d3
    .forceSimulation(visibleNodes)
    .force(
      'link',
      d3
        .forceLink(visibleLinks)
        .id((d) => d.id)
        .distance(105)
        .strength(0.65),
    )
    .force('charge', d3.forceManyBody().strength(-250))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force(
      'collision',
      d3.forceCollide().radius((d) => d.size + 34),
    )
    .on('tick', () => {
      const updateLine = function (d) {
        const dx = d.target.x - d.source.x;
        const dy = d.target.y - d.source.y;
        const distance = Math.max(Math.hypot(dx, dy), 1);
        const unitX = dx / distance;
        const unitY = dy / distance;
        const sourceOffset = d.source.size + 5;
        const targetOffset = d.target.size + 8;
        d3.select(this)
          .attr('x1', d.source.x + unitX * sourceOffset)
          .attr('y1', d.source.y + unitY * sourceOffset)
          .attr('x2', d.target.x - unitX * targetOffset)
          .attr('y2', d.target.y - unitY * targetOffset);
      };
      linkHitArea.each(updateLine);
      link.each(updateLine);
      node.attr('transform', (d) => `translate(${d.x},${d.y})`);
    });
}

function selectNode(nodeData) {
  selectedId = nodeData.id;
  d3.selectAll('.node').classed('is-selected', (d) => d.id === selectedId);
  const endpointId = (endpoint) =>
    isString(endpoint) ? endpoint : endpoint.id;
  const neighbors = links
    .filter(
      (link) =>
        endpointId(link.source) === selectedId ||
        endpointId(link.target) === selectedId,
    )
    .map((link) => ({
      other:
        endpointId(link.source) === selectedId
          ? endpointById(endpointId(link.target))
          : endpointById(endpointId(link.source)),
      type: link.type,
    }));
  document.querySelector('#inspector-index').textContent = String(
    nodes.findIndex((node) => node.id === selectedId) + 1,
  ).padStart(2, '0');
  const roleLabel = nodeData.role === 'inter-stem' ? 'inter-stem' : 'node';
  document.querySelector('#inspector-content').innerHTML =
    `<span class="tag">${roleLabel} / ${nodeData.domain} / ${nodeData.kind}</span><h2>${nodeData.label}</h2><p class="description">${nodeData.text}</p><ul class="relation-list">${neighbors.map(({ other, type }) => `<li>${other.label}<span>${type}</span></li>`).join('')}</ul>`;
}

function endpointById(id) {
  return nodes.find((node) => node.id === id);
}

function showTooltip(event, nodeData) {
  tooltip
    .attr('aria-hidden', 'false')
    .html(
      `<strong>${nodeData.label}</strong><span>${nodeData.role === 'inter-stem' ? 'inter-stem node' : nodeData.kind}</span><p>${nodeData.text}</p>`,
    );
  moveTooltip(event);
}

function relationLabel(linkData) {
  const source = endpointById(
    isString(linkData.source) ? linkData.source : linkData.source.id,
  );
  const target = endpointById(
    isString(linkData.target) ? linkData.target : linkData.target.id,
  );
  return `${source.label} ${linkData.type} ${target.label}`;
}

function showRelationTooltip(event, linkData) {
  const source = endpointById(
    isString(linkData.source) ? linkData.source : linkData.source.id,
  );
  const target = endpointById(
    isString(linkData.target) ? linkData.target : linkData.target.id,
  );
  const direction =
    linkData.direction === 'both' ? 'both directions' : 'forward direction';
  const relationArrow = linkData.direction === 'both' ? '↔' : '→';
  const text =
    relationText[`${source.id}|${target.id}`] ||
    relationDescriptions[linkData.type];
  tooltip
    .attr('aria-hidden', 'false')
    .html(
      `<strong>${source.label} ${relationArrow} ${target.label}</strong><span>${linkData.type} / ${direction}</span><p>${text}</p>`,
    );
  moveTooltip(event);
}

function moveTooltip(event) {
  const bounds = mapFrame.getBoundingClientRect();
  const tooltipWidth = 270;
  const left = Math.min(
    event.clientX - bounds.left + 18,
    bounds.width - tooltipWidth - 12,
  );
  const top = Math.max(event.clientY - bounds.top - 18, 12);
  tooltip.style('left', `${Math.max(left, 12)}px`).style('top', `${top}px`);
}

function hideTooltip() {
  tooltip.attr('aria-hidden', 'true');
}

function initializeViewBox(width, height) {
  svg.attr('viewBox', `0 0 ${width} ${height}`);
  svg.selectAll('*').remove();
}

function dragStarted(event, d) {
  if (!event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}
function dragged(event, d) {
  d.fx = event.x;
  d.fy = event.y;
}
function dragEnded(event, d) {
  if (!event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
function isString(value) {
  return typeof value === 'string' || value instanceof String;
}

function resetInspector() {
  document.querySelector('#inspector-index').textContent = '00';
  document.querySelector('#inspector-content').innerHTML =
    '<p class="select-prompt">Select a concentration to follow its relations and tensions.</p><div class="signal-line"></div><p class="small-copy">Scale, color, and proximity are decisions made by the map. Movement keeps the configuration open.</p>';
}

document.querySelectorAll('.filter').forEach((button) =>
  button.addEventListener('click', () => {
    let selectedDomain = button.dataset.domain;
    console.log(activeDomains);
    if (selectedDomain === 'all') {
      activeDomains = new Set(['all']);
    } else {
      activeDomains.delete('all');
      if (activeDomains.has(selectedDomain)) {
        activeDomains.delete(selectedDomain);
      } else {
        activeDomains.add(selectedDomain);
      }
      if (activeDomains.size === 0) {
        activeDomains.add('all');
      }
    }

    if (activeDomains.size === 4) {
      activeDomains = new Set(['all']);
    }

    document
      .querySelectorAll('.filter')
      .forEach((item) =>
        item.classList.toggle(
          'is-active',
          activeDomains.has(item.dataset.domain),
        ),
      );
    selectedId = null;
    resetInspector();
    render();
  }),
);
document.querySelector('#reset').addEventListener('click', () => {
  activeDomains = new Set(['all']);
  selectedId = null;
  document
    .querySelectorAll('.filter')
    .forEach((item) =>
      item.classList.toggle('is-active', item.dataset.domain === 'all'),
    );
  resetInspector();
  render();
});
window.addEventListener('resize', render);
render();
