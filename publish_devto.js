const fs = require('fs');
const fetch = require('node-fetch');

/**
 * Publish an article to Dev.to.
 * @param {Object} options
 * @param {string} options.title - Title of the article.
 * @param {string} options.draftPath - Path to markdown file containing the article body.
 * @param {string} options.apiKey - Dev.to API key (use DEVTO_API_KEY env var if omitted).
 * @param {string[]} [options.tags] - Optional tags.
 * @returns {Promise<string>} URL of the published article.
 */
async function publishArticle({ title, draftPath, apiKey, tags = [] }) {
  const key = apiKey || process.env.DEVTO_API_KEY;
  if (!key) {
    throw new Error('Dev.to API key is required');
  }
  const body = fs.readFileSync(draftPath, 'utf8');
  const response = await fetch('https://dev.to/api/articles', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'api-key': key,
    },
    body: JSON.stringify({
      article: {
        title,
        published: true,
        body_markdown: body,
        tags,
      },
    }),
  });

  if (!response.ok) {
    const err = await response.text();
    throw new Error(`Failed to publish article: ${response.status} ${err}`);
  }
  const data = await response.json();
  return data.url;
}

module.exports = { publishArticle };
