PORTNAME=	voltron
DISTVERSION=	v0.1.8.r0.gbe9e54b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	UI for GDB, LLDB and Vivisects VDB.
WWW=		https://github.com/snare/voltron

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-blessed@${PY_FLAVOR} \
		??/py-flask-restful@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-nose@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pysigset@${PY_FLAVOR} \
		??/py-requests-unixsocket@${PY_FLAVOR} \
		??/py-scruffington@${PY_FLAVOR} \
		??/py-scruffy@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
