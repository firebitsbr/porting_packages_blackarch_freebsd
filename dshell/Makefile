PORTNAME=	dshell
DISTVERSION=	142.695c891
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A network forensic analysis framework.
WWW=		https://github.com/USArmyResearchLab/Dshell

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-dpkt@${PY_FLAVOR} \
		??/py-elasticsearch@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		devel/git \
		lang/python3

RUN_DEPENDS=	??/elasticsearch \
		??/geoip \
		??/py-dpkt@${PY_FLAVOR} \
		??/py-elasticsearch@${PY_FLAVOR} \
		??/py-geoip@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		??/py-pypcap@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
