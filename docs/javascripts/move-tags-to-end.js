// Move Material "tags chips" from top of post to bottom
(() => {
  const moveTagsToEnd = () => {
    const article = document.querySelector("article.md-content__inner.md-typeset");
    if (!article) return;

    // On post pages, tags are injected as the first top-level element
    const tags = article.querySelector(":scope > nav.md-tags");
    if (!tags) return;

    tags.classList.add("md-tags--end");
    article.appendChild(tags);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", moveTagsToEnd);
  } else {
    moveTagsToEnd();
  }
})();

