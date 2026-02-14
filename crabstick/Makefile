PORTNAME=	crabstick
DISTVERSION=	47.bb7827f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automatic remote/local file inclusion vulnerability analysis and exploit tool.
WWW=		https://github.com/Hack-Hut/CrabStick

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-docopt@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
