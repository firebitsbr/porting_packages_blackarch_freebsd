PORTNAME=	machinae
DISTVERSION=	197.9ef3e6c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for collecting intelligence from public sites/feeds about various security-related pieces of data.
WWW=		https://github.com/HurricaneLabs/machinae

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-defang@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-feedparser@${PY_FLAVOR} \
		??/py-filemagic@${PY_FLAVOR} \
		??/py-html5lib@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-relatime@${PY_FLAVOR} \
		??/py-stopit@${PY_FLAVOR} \
		??/py-tzlocal@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
