PORTNAME=	anti-xss
DISTVERSION=	v0.1.alpha.r69.g2725dc9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A XSS vulnerability scanner.
WWW=		https://github.com/lewangbtcc/anti-XSS

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-reportlab@${PY_FLAVOR} \
		??/py-tornado@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
