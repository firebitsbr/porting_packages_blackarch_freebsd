PORTNAME=	fbht
DISTVERSION=	70.d75ae93
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Facebook Hacking Tool
WWW=		https://github.com/chinoogawa/fbht

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-matplotlib@${PY_FLAVOR} \
		??/py-mechanize@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
