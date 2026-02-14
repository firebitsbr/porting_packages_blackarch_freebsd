PORTNAME=	fastnetmon
DISTVERSION=	v1.2.8.r40.ga2d2d0d7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	High performance DoS/DDoS load analyzer built on top of multiple packet capture engines.
WWW=		https://github.com/pavel-odintsov/fastnetmon

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/binutils \
		??/boost \
		??/cmake \
		??/hiredis \
		??/libbpf \
		??/libpfring \
		??/log4cpp \
		??/luajit \
		??/make \
		??/mongo-c-driver \
		??/ndpi \
		??/numactl \
		devel/git

RUN_DEPENDS=	??/binutils \
		??/boost \
		??/boost-libs \
		??/capnproto \
		??/grpc \
		??/hiredis \
		??/json-c \
		??/libpfring \
		??/log4cpp \
		??/luajit \
		??/mongo-c-driver \
		??/ndpi \
		??/numactl \
		??/pfring-dkms


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
