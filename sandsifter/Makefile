PORTNAME=	sandsifter
DISTVERSION=	2.8375e61
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The x86 processor fuzzer.
WWW=		https://github.com/xoreaxeaxeax/sandsifter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/make \
		??/sed \
		devel/git

RUN_DEPENDS=	??/capstone \
		??/py-argparse@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
