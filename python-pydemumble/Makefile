PORTNAME=	python-pydemumble
DISTVERSION=	0.0.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python wrapper library for demumble; demumble is a tool to demangle C++, Rust, and Swift symbol names.
WWW=		https://pypi.org/project/pydemumble/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/nanobind \
		??/py-scikit-build-core@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
