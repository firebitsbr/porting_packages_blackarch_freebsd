PORTNAME=	pyinstaller
DISTVERSION=	6.18.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Bundles a Python application and all its dependencies into a single package.
WWW=		https://pyinstaller.org

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/# \
		??/bootloader \
		??/package \
		??/py-build@${PY_FLAVOR} \
		??/py-hatchling@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		??/waf \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python

RUN_DEPENDS=	??/# \
		??/base-devel \
		??/binutils \
		??/dependencies \
		??/gcc \
		??/project \
		??/py-altgraph@${PY_FLAVOR} \
		??/pyinstaller-hooks-contrib \
		??/system \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
