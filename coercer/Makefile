PORTNAME=	coercer
DISTVERSION=	2.4.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Coerce a Windows server to authenticate on an arbitrary machine through 15 methods.
WWW=		https://github.com/p0dalirius/Coercer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-xlsxwriter@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
