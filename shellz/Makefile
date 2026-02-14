PORTNAME=	shellz
DISTVERSION=	161.0ed068f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A script for generating common revshells fast and easy.
WWW=		https://github.com/4ndr34z/shells

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/jq \
		??/ngrok \
		??/openbsd-netcat \
		??/py-updog@${PY_FLAVOR} \
		??/rlwrap \
		devel/py-pip@${PY_FLAVOR} \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
