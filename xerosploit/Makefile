PORTNAME=	xerosploit
DISTVERSION=	38.e2c3c7b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Efficient and advanced man in the middle framework.
WWW=		https://github.com/LionSec/xerosploit

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/bettercap \
		??/hping \
		??/iproute2 \
		??/net-tools \
		??/py-recommonmark@${PY_FLAVOR} \
		??/py-sphinx_rtd_theme@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		??/wireless_tools \
		lang/python3 \
		lang/ruby \
		security/nmap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
