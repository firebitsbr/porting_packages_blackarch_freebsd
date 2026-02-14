PORTNAME=	whatbreach
DISTVERSION=	42.dad6b9f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OSINT tool to find breached emails and databases.
WWW=		https://github.com/ekultek/whatbreach

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-arrow@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
