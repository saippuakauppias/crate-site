from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import evaluator
evaluator.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer

from search.views import Search


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", Search.as_view(), name="home"),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^about/", include("about.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/", include(PinaxConsumer().urls)),
    url(r"^profiles/", include("idios.urls")),
    # url(r"^notices/", include("notification.urls")),
    url(r"^announcements/", include("announcements.urls")),
    url(r"^admin_tools/", include("admin_tools.urls")),

    url(r"^packages/", include("packages.urls")),
    url(r"^favorites/", include("favorites.urls")),
    url(r"^help/", include("helpdocs.urls")),
    url(r"^api/", include("crate_project.api_urls")),

    url(r"^s/(?P<path>.+)?", "crate.views.simple_redirect", name="simple_redirect"),

    url(r"^", include("search.urls")),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
