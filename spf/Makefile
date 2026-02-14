PORTNAME=	spf
DISTVERSION=	85.344ac2f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A python tool designed to allow for quick recon and deployment of simple social engineering phishing exercises.
WWW=		https://github.com/tatanus/SPF

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/phantomjs \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-twisted@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
