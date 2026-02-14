PORTNAME=	rawsec-cli
DISTVERSION=	1.2.0.r7.gf7a08c6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Rawsec Inventory search CLI to find security tools and resources.
WWW=		https://github.com/mBouamama/rawsec_cli

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-columnar@${PY_FLAVOR} \
		??/py-gitpython@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
