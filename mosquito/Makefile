PORTNAME=	mosquito
DISTVERSION=	39.fe54831
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	XSS exploitation tool - access victims through HTTP proxy.
WWW=		https://github.com/koto/mosquito

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-flask@${PY_FLAVOR} \
		??/py-jsbeautifier@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pyasn1-modules@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-urwid@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
