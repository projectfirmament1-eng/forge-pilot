const { publishArticle } = require('./publish_devto');
const fetch = require('node-fetch');

jest.mock('node-fetch', () => jest.fn());

describe('publishArticle', () => {
  const dummyUrl = 'https://dev.to/username/future-of-wearables';
  const mockResponse = {
    ok: true,
    json: async () => ({ url: dummyUrl }),
  };

  beforeEach(() => {
    fetch.mockResolvedValue(mockResponse);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it('posts article and returns URL', async () => {
    const title = 'The Future of Wearables';
    const draftPath = './future-of-wearables.md';
    const apiKey = 'test-key';
    const url = await publishArticle({ title, draftPath, apiKey, tags: ['tech'] });
    expect(url).toBe(dummyUrl);
    expect(fetch).toHaveBeenCalledWith('https://dev.to/api/articles', expect.objectContaining({
      method: 'POST',
      headers: expect.objectContaining({ 'api-key': apiKey }),
    }));
  });
});
