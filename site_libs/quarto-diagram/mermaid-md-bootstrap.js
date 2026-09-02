// Upgrade Pandoc ```mermaid fences in .md pages to Quarto's mermaid-js format.
(function () {
  function bootstrapMermaidPres() {
    for (const pre of document.querySelectorAll("pre.mermaid:not(.mermaid-js)")) {
      const code = pre.querySelector("code");
      const text = (code ? code.textContent : pre.textContent).replaceAll("\u00a0", " ");
      pre.textContent = text.trim();
      pre.classList.add("mermaid-js");
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootstrapMermaidPres);
  } else {
    bootstrapMermaidPres();
  }
})();
