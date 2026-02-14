PORTNAME=	dorknet
DISTVERSION=	58.419d6a2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Selenium powered Python script to automate searching for vulnerable web apps.
WWW=		https://github.com/NullArray/DorkNet

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-blessings@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
