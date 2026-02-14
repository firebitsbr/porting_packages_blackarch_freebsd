PORTNAME=	python-pyperscan
DISTVERSION=	v0.3.0.r151.g25c2f5b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python binding for Hyperscan.
WWW=		https://github.com/vlaci/pyperscan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/clang \
		??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		lang/rust

RUN_DEPENDS=	??/hyperscan \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
