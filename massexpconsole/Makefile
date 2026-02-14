PORTNAME=	massexpconsole
DISTVERSION=	v2.3.5.r1.g530c880
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A collection of tools and exploits with a cli ui for mass exploitation.
WWW=		https://github.com/jm33-m0/massExpConsole

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-docopt@${PY_FLAVOR} \
		??/py-html5lib@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
