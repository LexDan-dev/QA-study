from playwright.sync_api import Page, expect

# --- Константы: URL и локаторы ---
TOPICS_URL = "https://github.com/topics"

# Каждая карточка топика — ссылка на /topics/<slug>.
# Цепляемся за href, а НЕ за длинное имя из codegen (оно хрупкое).
TOPIC_LINK = 'a[href^="/topics/"]'


class GitHubTopicsPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(TOPICS_URL)
        self.page.wait_for_load_state("networkidle")
        return self

    def should_have_topics_section(self):
        # секция присутствует: хотя бы одна карточка-топик видна
        expect(self.page.locator(TOPIC_LINK).first).to_be_visible()
        return self

    def get_topic_slugs(self):
        # авто-ждём появления списка, потом снимаем снапшот ссылок
        expect(self.page.locator(TOPIC_LINK).first).to_be_visible()
        slugs = set()
        for link in self.page.locator(TOPIC_LINK).all():
            href = link.get_attribute("href") or ""
            slug = href.split("/topics/")[-1].split("?")[0].strip("/")
            if slug:
                slugs.add(slug)
        return slugs
