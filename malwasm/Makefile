PORTNAME=	malwasm
DISTVERSION=	0.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Offline debugger for malwares reverse engineering.
WWW=		https://github.com/malwarelu/malwasm

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/cuckoo \
		??/postgresql \
		??/py-flask@${PY_FLAVOR} \
		??/py-progressbar@${PY_FLAVOR} \
		??/py-psycopg2@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
