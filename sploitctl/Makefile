PORTNAME=	sploitctl
DISTVERSION=	3.0.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Fetch, install and search exploit archives from exploit sites like exploit-db and packetstorm.
WWW=		https://github.com/BlackArch/sploitctl

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/py-pygit2@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
