PORTNAME=	httpscreenshot
DISTVERSION=	70.f081c69
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for grabbing screenshots and HTML of large numbers of websites.
WWW=		https://github.com/breenmachine/httpscreenshot

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-libnmap@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-m2crypto@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pyvirtualdisplay@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-webdriver-manager@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
