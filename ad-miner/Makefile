PORTNAME=	ad-miner
DISTVERSION=	v1.8.1.r0.g6467f51
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Active Directory audit tool that extract data from Bloodhound to uncover security weaknesses and generate an HTML report
WWW=		https://github.com/Mazars-Tech/AD_Miner

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-poetry@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
