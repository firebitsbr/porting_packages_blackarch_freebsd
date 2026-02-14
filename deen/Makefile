PORTNAME=	deen
DISTVERSION=	601.fd9aebe
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Generic data encoding/decoding application built with PyQt5.
WWW=		https://github.com/takeshixx/deen

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-bcrypt@${PY_FLAVOR} \
		??/py-dicttoxml@${PY_FLAVOR} \
		??/py-jose@${PY_FLAVOR} \
		??/py-jsbeautifier@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pyqt5@${PY_FLAVOR} \
		??/py-xmltodict@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
