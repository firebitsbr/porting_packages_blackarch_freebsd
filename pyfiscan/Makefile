PORTNAME=	pyfiscan
DISTVERSION=	3002.bea806a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Free web-application vulnerability and version scanner.
WWW=		https://github.com/fgeek/pyfiscan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-chardet@${PY_FLAVOR} \
		??/py-docopt@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-scandir@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
