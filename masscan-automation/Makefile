PORTNAME=	masscan-automation
DISTVERSION=	26.a170abc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Masscan integrated with Shodan API.
WWW=		https://github.com/trevordavenport/MasscanAutomation

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/masscan \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
