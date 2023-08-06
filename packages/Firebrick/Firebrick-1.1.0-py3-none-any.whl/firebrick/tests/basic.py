from firebrick.tests.test import (
    ResolveUrlTest,
    GetViewTest,
    GetViewOr404Test
)


class BasicGETViewTest(ResolveUrlTest, GetViewTest):
    pass


class BasicGETOr404ViewTest(ResolveUrlTest, GetViewOr404Test):
    pass