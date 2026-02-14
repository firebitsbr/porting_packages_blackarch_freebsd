PORTNAME=	cr3dov3r
DISTVERSION=	48.49bbdbe
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Search for public leaks for email addresses + check creds against 16 websites.
WWW=		https://github.com/D4Vinci/Cr3dOv3r

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-mechanicalsoup@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
