PORTNAME=	zelos
DISTVERSION=	272.506554d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A comprehensive binary emulation and instrumentation platform.
WWW=		https://github.com/zeropointdynamics/zelos

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/lief \
		??/py-capstone@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-coloredlogs@${PY_FLAVOR} \
		??/py-configargparse@${PY_FLAVOR} \
		??/py-dnslib@${PY_FLAVOR} \
		??/py-dpkt@${PY_FLAVOR} \
		??/py-hexdump@${PY_FLAVOR} \
		??/py-lark-parser@${PY_FLAVOR} \
		??/py-pypacker@${PY_FLAVOR} \
		??/py-sortedcontainers@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-unicorn@${PY_FLAVOR} \
		??/py-verboselogs@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		??/py-zebracorn@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
