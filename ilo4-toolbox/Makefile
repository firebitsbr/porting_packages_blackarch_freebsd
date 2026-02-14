PORTNAME=	ilo4-toolbox
DISTVERSION=	47.672a5d6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Toolbox for HPE iLO4 analysis.
WWW=		https://github.com/airbus-seclab/ilo4_toolbox

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-keystone@${PY_FLAVOR} \
		lang/go \
		lang/python3 \
		lang/ruby \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
