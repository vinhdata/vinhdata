# VinhData — Data Engineer Portfolio & Knowledge Base

A portfolio and knowledge base website built with MkDocs and Material theme, deployed to GitHub Pages.

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd vinhdata
```

2. Install dependencies:
```bash
uv sync
```

### Local Development

Run the development server:
```bash
uv run mkdocs serve
```

The site will be available at `http://127.0.0.1:8000`

### Build

Build the static site:
```bash
uv run mkdocs build
```

The built site will be in the `site/` directory.

## Deployment

This site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch.

### Setup GitHub Pages

1. Go to your repository settings
2. Navigate to **Pages** section
3. Under **Source**, select **GitHub Actions**

The GitHub Actions workflow (`.github/workflows/deploy.yml`) will automatically build and deploy your site.

## Project Structure

```
vinhdata/
├── docs/                    # Documentation source files
│   ├── index.md            # Home page
│   ├── about.md            # About page
│   ├── portfolio/          # Portfolio section
│   └── knowledge-base/     # Knowledge base articles
│       ├── data-engineering/
│       ├── infrastructure/
│       └── databases/
├── mkdocs.yml              # MkDocs configuration
├── pyproject.toml          # Python project configuration
└── .github/workflows/      # GitHub Actions workflows
```

## Adding Content

### Add a New Article

1. Create a new markdown file in the appropriate section under `docs/`
2. Update `mkdocs.yml` navigation if needed
3. Commit and push to deploy

### Customize

- Edit `mkdocs.yml` to customize site settings, theme, and navigation
- Modify theme colors, fonts, and features in the `theme` section
- Add plugins and markdown extensions as needed

## License

[Add your license here]
