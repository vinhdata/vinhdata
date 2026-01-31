---
date: 2026-01-29
categories:
  - How-To
tags:
  - mkdocs
  - github-actions
  - github-pages
  - portfolio
  - uv
  - tutorial
---

# How to Setup a Portfolio Website with MkDocs and GitHub Actions

This guide walks through setting up a portfolio and knowledge base website using MkDocs Material theme, managed with `uv`, and automatically deployed to GitHub Pages using GitHub Actions.

<!-- more -->

## Overview

**What we'll build:**
- A static documentation site using MkDocs
- Beautiful Material Design theme
- Automatic deployment to GitHub Pages on every push
- Fast dependency management with `uv`

**Tech Stack:**
- [MkDocs](https://www.mkdocs.org/) - Static site generator
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Modern theme
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager
- [GitHub Actions](https://github.com/features/actions) - CI/CD
- [GitHub Pages](https://pages.github.com/) - Free hosting

## Prerequisites

- Python 3.13+
- `uv` installed ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- GitHub account
- Git installed

## Step 1: Initialize Project with uv

First, create a new directory and initialize it with `uv`:

```bash
mkdir my-portfolio
cd my-portfolio
uv init
```

This creates:
- `pyproject.toml` - Project configuration
- `.python-version` - Python version specification
- `main.py` - Starter Python file (we'll remove this)

## Step 2: Install MkDocs and Material Theme

Add MkDocs and the Material theme as dependencies:

```bash
uv add mkdocs mkdocs-material
```

This will:
- Install all necessary packages
- Create a virtual environment in `.venv/`
- Generate `uv.lock` file for reproducible builds

## Step 3: Create MkDocs Configuration

Create `mkdocs.yml` in the project root:

```yaml
site_name: My Portfolio
site_description: Portfolio and knowledge base
site_author: Your Name
site_url: https://yourusername.github.io/repository-name

repo_name: repository-name
repo_url: https://github.com/yourusername/repository-name

theme:
  name: material
  palette:
    # Light mode
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    # Dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - navigation.tracking
    - search.suggest
    - search.highlight
    - content.code.copy
  language: en

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.mark
  - attr_list
  - pymdownx.tabbed:
      alternate_style: true
  - toc:
      permalink: true

nav:
  - Home: index.md
  - About: about.md
  - Portfolio:
    - portfolio/index.md
  - Knowledge Base:
    - knowledge-base/index.md

plugins:
  - search
```

## Step 4: Create Documentation Structure

Create the docs directory and initial pages:

```bash
mkdir -p docs/portfolio docs/knowledge-base
```

Create `docs/index.md`:

```markdown
# Welcome

Portfolio and knowledge base website.

## Navigation

- [Portfolio](portfolio/index.md)
- [Knowledge Base](knowledge-base/index.md)
- [About](about.md)
```

Create `docs/about.md`:

```markdown
# About

About this site and the author.
```

Create `docs/portfolio/index.md`:

```markdown
# Portfolio

Projects will be added here.
```

Create `docs/knowledge-base/index.md`:

```markdown
# Knowledge Base

Technical articles and guides.
```

## Step 5: Test Locally

Run the development server:

```bash
uv run mkdocs serve
```

Visit `http://127.0.0.1:8000` to preview your site. The server will auto-reload when you edit files.

Build the static site:

```bash
uv run mkdocs build
```

## Step 6: Create GitHub Actions Workflow

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy MkDocs to GitHub Pages

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version-file: ".python-version"

      - name: Install dependencies
        run: uv sync

      - name: Build MkDocs site
        run: uv run mkdocs build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./site

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

## Step 7: Clean Up Unused Files

Remove the default `main.py` file since it's not needed:

```bash
rm main.py
```

## Step 8: Initialize Git Repository

If you haven't already:

```bash
git init
git add .
git commit -m "Initialize MkDocs project with Material theme"
```

## Step 9: Push to GitHub

Create a repository on GitHub, then:

```bash
git remote add origin git@github.com:yourusername/repository-name.git
git branch -M main
git push -u origin main
```

## Step 10: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Click **Pages** in the left sidebar (under "Code and automation")
4. Under "Build and deployment":
   - For **Source**, select **"GitHub Actions"**
5. The page will auto-save

## Step 11: Wait for Deployment

1. Go to the **Actions** tab in your repository
2. You should see the workflow running
3. Wait for it to complete (usually 1-2 minutes)
4. Your site will be live at: `https://yourusername.github.io/repository-name/`

## Project Structure

```
my-portfolio/
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions workflow
├── docs/                    # Your content
│   ├── index.md
│   ├── about.md
│   ├── portfolio/
│   │   └── index.md
│   └── knowledge-base/
│       └── index.md
├── mkdocs.yml              # MkDocs configuration
├── pyproject.toml          # Python dependencies
├── uv.lock                 # Locked dependencies
├── .python-version         # Python version
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

## Adding Content

### Add a New Article

1. Create a markdown file in the appropriate section:
```bash
touch docs/knowledge-base/my-article.md
```

2. Edit the file with your content

3. Update `mkdocs.yml` navigation:
```yaml
nav:
  - Knowledge Base:
    - knowledge-base/index.md
    - My Article: knowledge-base/my-article.md
```

4. Commit and push:
```bash
git add .
git commit -m "Add new article"
git push
```

The site automatically rebuilds and deploys!

## Customization

### Change Colors

Edit `mkdocs.yml`:

```yaml
theme:
  palette:
    - scheme: default
      primary: teal        # Change this
      accent: amber        # And this
```

Available colors: red, pink, purple, indigo, blue, teal, green, amber, orange, brown

### Add More Features

Material theme has many features. Add to `theme.features`:

```yaml
features:
  - navigation.instant    # Instant loading
  - navigation.tracking   # URL tracking
  - toc.follow           # Follow table of contents
  - navigation.footer    # Add footer navigation
```

### Enable Blog Plugin (Optional)

For a blog-like structure:

```bash
uv add mkdocs-material[blog]
```

## Maintenance

### Update Dependencies

```bash
uv sync --upgrade
```

### Local Development

Always test locally before pushing:

```bash
uv run mkdocs serve
```

## Troubleshooting

### Deployment Fails with 404 Error

**Error**: "Failed to create deployment (status: 404)"

**Solution**: Ensure GitHub Pages is enabled with "GitHub Actions" as the source in repository settings.

### Build Fails

Check the Actions tab for detailed error logs. Common issues:
- Missing files referenced in navigation
- Invalid YAML syntax in `mkdocs.yml`
- Missing dependencies

### Site Not Updating

- Check Actions tab to ensure workflow completed successfully
- Clear browser cache (Cmd/Ctrl + Shift + R)
- Wait a few minutes for GitHub's CDN to update

## Next Steps

1. **Update `mkdocs.yml`** with your actual repository URL
2. **Customize the theme** with your preferred colors and features
3. **Add your content** - articles, projects, tutorials
4. **Add a custom domain** (optional) in GitHub Pages settings

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Modern theme
- [uv Documentation](https://docs.astral.sh/uv/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

## Conclusion

You now have a modern, automatically-deployed portfolio website! Every time you push to the `main` branch, GitHub Actions will build and deploy your site. Focus on creating great content - the infrastructure handles itself.

