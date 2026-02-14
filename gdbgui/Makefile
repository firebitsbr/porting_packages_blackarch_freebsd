PORTNAME=	gdbgui
DISTVERSION=	438.773b916
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Browser-based gdb frontend using Flask and JavaScript to visually debug C, C++, Go, or Rust.
WWW=		https://github.com/cs01/gdbgui

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/yarn \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/gdb \
		??/py-brotli@${PY_FLAVOR} \
		??/py-enum-compat@${PY_FLAVOR} \
		??/py-eventlet@${PY_FLAVOR} \
		??/py-flask-compress@${PY_FLAVOR} \
		??/py-flask-socketio@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-pygdbmi@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pypugjs@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
