PORTNAME=	vmcloak
DISTVERSION=	955.fae1f29
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automated Virtual Machine Generation and Cloaking for Cuckoo Sandbox.
WWW=		https://github.com/Cryss76/vmcloak

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-pytest@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/cdrtools \
		??/dmidecode \
		??/lshw \
		??/py-alembic@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-lockfile@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/qemu-full \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
