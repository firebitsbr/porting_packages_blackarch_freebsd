PORTNAME=	checkov
DISTVERSION=	3.2.500.r1.ga26172e42
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Prevent cloud misconfigurations and find vulnerabilities during build-time in infrastructure as code, container images and open source packages.
WWW=		https://github.com/bridgecrewio/checkov

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-virtualenv@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
