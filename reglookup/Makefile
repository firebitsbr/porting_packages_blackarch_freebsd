PORTNAME=	reglookup
DISTVERSION=	1.0.1+svn296.2.r0.gcab83db
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Command line utility for reading and querying Windows NT registries.
WWW=		https://projects.sentinelchicken.org/reglookup

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/docbook-utils \
		??/docbook2x \
		??/gcc \
		??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		??/scons \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/talloc \
		lang/python \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
