PORTNAME=	triton
DISTVERSION=	4324.4f7ddb77
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Dynamic Binary Analysis (DBA) framework.
WWW=		https://github.com/JonathanSalwan/Triton

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/boost \
		??/capstone \
		??/z3 \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
