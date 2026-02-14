PORTNAME=	pastejacker
DISTVERSION=	12.ed9f153
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Hacking systems with the automation of PasteJacking attacks.
WWW=		https://github.com/D4Vinci/PasteJacker

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/metasploit \
		??/ncurses \
		??/py-gnureadline@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
