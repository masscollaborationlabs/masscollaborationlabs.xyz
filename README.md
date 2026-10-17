# Mass Collaboration Labs Website

Source code for the Mass Collaboration Labs website, a responsive static landing page available in Turkish and English.

## Features

- Responsive layout with clear links to the organization's work and YouTube channel.
- Turkish and English language toggle that updates page text, metadata, and accessibility labels.
- Privacy-enhanced YouTube video embed with lazy loading and no autoplay.
- Search and social sharing metadata, an SVG logo source, an optimized WebP logo, and a PNG favicon.
- LiteSpeed/Apache security response headers configured in the root `.htaccess` file.
- Dependency-free site checks that run locally and in GitHub Actions.

## Local Preview

Open `index.html` in a browser, or serve the repository with a local static web server. The page loads its CSS, JavaScript, and images from this repository and embeds its introduction video from YouTube.

## Validation

Run the static checks with Python 3:

```sh
python3 scripts/check_site.py
```

The same check runs in GitHub Actions for pushes and pull requests. It checks the HTML structure, local asset references, image and iframe labels, lazy loading, external-link safety, and SVG syntax.

## LiteSpeed Security Headers

The root `.htaccess` configures security response headers for LiteSpeed or Apache when `mod_headers` and `.htaccess` overrides are enabled for the document root. HSTS is intended for HTTPS and does not include subdomains. The Content Security Policy is also present in `index.html`; keep the two policies synchronized.

After deployment, verify the response headers over HTTPS:

```sh
curl -I https://your-domain/
```

## Recent Changes

- Replaced the oversized display logo with a 240-pixel WebP asset and added a 64-pixel PNG favicon while preserving the original SVG sources.
- Added lazy loading to the YouTube iframe and removed autoplay.
- Added LiteSpeed/Apache security headers and documented the deployment requirements.
- Added dependency-free static site checks and a GitHub Actions workflow.
- Added Turkish and English page content, search and social metadata, clearer navigation, and a consolidated PlusClouds banner.
- Added the full AGPL-3.0-or-later notice to project-owned source files.

See [ChangeLog](./ChangeLog) for the complete change summary.

## License

Website source code of Mass Collaboration Labs

Copyright (C) 2026 Mass Collaboration Labs

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
