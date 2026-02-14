PORTNAME=	pasv-agrsv
DISTVERSION=	57.6bb54f7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Passive recon / OSINT automation script.
WWW=		https://github.com/isaudits/pasv-agrsv

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-elixir@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
