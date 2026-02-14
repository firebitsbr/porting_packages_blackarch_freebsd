PORTNAME=	striker
DISTVERSION=	85.87c184d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An offensive information and vulnerability scanner.
WWW=		https://github.com/UltimateHackers/Striker

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		??/py-mechanize@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
