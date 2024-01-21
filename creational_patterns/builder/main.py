from creational_patterns.builder.article_director import ArticleDirector
from creational_patterns.builder.txt_builder import TXTBuilder
from creational_patterns.builder.xml_builder import XMLBuilder

article = {
    "title": "The Importance of Sleep for Cognitive Functioning",
    "authors": ["Smith, John", "Johnson, Sarah"],
    "text": "Sleep is a vital component of human health and well-being. "
    "It is essential for proper cognitive functioning, "
    "including memory consolidation, learning, and decision-making. "
    "Lack of sleep can lead to a range of negative outcomes, "
    "including impaired cognitive performance, mood disturbances, "
    "and increased risk of accidents."
    "\n\n"
    "In this article, we review the current literature on "
    "the importance of sleep for cognitive functioning. "
    "We discuss the effects of sleep deprivation on "
    "cognitive performance and the mechanisms underlying these effects. "
    "We also examine the role of sleep in memory consolidation and learning, "
    "as well as the impact of sleep on decision-making and creativity."
    "\n\n"
    "Overall, our review highlights the critical role of sleep in "
    "cognitive functioning and underscores the importance of getting "
    "adequate sleep for optimal health and well-being.",
    "hash_code": "5f4dcc3b5aa765d61d8327deb882cf99",
}

ArticleDirector(builder=TXTBuilder()).construct(**article)
ArticleDirector(builder=XMLBuilder()).construct(**article)
