PORTNAME=	xcat
DISTVERSION=	266.faaf8fe
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A command line tool to automate the exploitation of blind XPath injection vulnerabilities.
WWW=		https://github.com/orf/xcat

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiodns@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-appdirs@${PY_FLAVOR} \
		??/py-cchardet@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-ipgetter@${PY_FLAVOR} \
		??/py-logbook@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-xmltodict@${PY_FLAVOR} \
		??/py-xpath-expressions@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
