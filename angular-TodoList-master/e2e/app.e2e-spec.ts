import { ListPage } from './app.po';

describe('list App', () => {
  let page: ListPage;

  beforeEach(() => {
    page = new ListPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
