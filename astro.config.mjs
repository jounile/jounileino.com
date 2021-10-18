// Full Astro Configuration API Documentation:
// https://docs.astro.build/reference/configuration-reference

// @type-check enabled!
// VSCode and other TypeScript-enabled text editors will provide auto-completion,
// helpful tooltips, and warnings if your exported object is invalid.
// You can disable this by removing "@ts-check" and `@type` comments below.

// @ts-check
export default /** @type {import('astro').AstroUserConfig} */ ({
  // Enable the Preact renderer to support Preact JSX components.
  renderers: ['@astrojs/renderer-preact'],
  
  /** Options specific to `astro build` */
  buildOptions: {
    /** Your public domain, e.g.: https://my-site.dev/. Used to generate sitemaps and canonical URLs. */
    site: "https://jounileino.com/",
    /** Generate an automatically-generated sitemap for your build.
     * Default: true
     */
    sitemap: true,
    /**
     * Control the output file URL format of each page.
     *   If 'file', Astro will generate a matching HTML file (ex: "/foo.html") instead of a directory.
     *   If 'directory', Astro will generate a directory with a nested index.html (ex: "/foo/index.html") for each page.
     * Default: 'directory'
     */
    pageUrlFormat: 'file',
  },
});
