PORTNAME=	clairvoyance
DISTVERSION=	2.5.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Obtain GraphQL API Schema even if the introspection is not enabled.
WWW=		https://github.com/nikitastupin/clairvoyance

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiohttp@${PY_FLAVOR} \
		??/py-asyncio@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
