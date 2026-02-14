PORTNAME=	spraycharles
DISTVERSION=	v2.0.2.r3.g131f8c6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Low and slow password spraying tool, designed to spray on an interval over a long period of time.
WWW=		https://github.com/Tw1sm/spraycharles

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-click-config-file@${PY_FLAVOR} \
		??/py-discord-webhook@${PY_FLAVOR} \
		??/py-notifiers@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pymsteams@${PY_FLAVOR} \
		??/py-requests-ntlm@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-texttable@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
